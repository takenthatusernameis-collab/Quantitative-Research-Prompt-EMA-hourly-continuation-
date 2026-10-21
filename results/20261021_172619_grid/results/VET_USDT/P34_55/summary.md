# EMA Hourly Continuation — VET/USDT P34_55

**Symbol:** VET/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 306 |
| net_profit_factor | 0.6226 |
| net_win_rate | 0.4804 |
| gross_profit_factor | 0.9179 |
| gross_win_rate | 0.4837 |
| sharpe_ratio | -2.5274 |
| sortino_ratio | -0.6337 |
| max_drawdown | 0.5327 |
| cagr | -0.2514 |
| net_avg_win | 57.9736 |
| net_avg_loss | -86.0918 |
| avg_hold_time_bars | 5.3137 |
| exposure | 0.0739 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
