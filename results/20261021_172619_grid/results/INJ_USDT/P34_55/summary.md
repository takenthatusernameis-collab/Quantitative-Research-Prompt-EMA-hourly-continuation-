# EMA Hourly Continuation — INJ/USDT P34_55

**Symbol:** INJ/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 306 |
| net_profit_factor | 0.7798 |
| net_win_rate | 0.5033 |
| gross_profit_factor | 1.0261 |
| gross_win_rate | 0.5033 |
| sharpe_ratio | -1.4492 |
| sortino_ratio | -0.3641 |
| max_drawdown | 0.3710 |
| cagr | -0.1536 |
| net_avg_win | 78.6817 |
| net_avg_loss | -102.2287 |
| avg_hold_time_bars | 5.4869 |
| exposure | 0.0763 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
