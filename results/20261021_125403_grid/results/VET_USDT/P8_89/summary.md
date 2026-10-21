# EMA Hourly Continuation — VET/USDT P8_89

**Symbol:** VET/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 498 |
| net_profit_factor | 0.9341 |
| net_win_rate | 0.5402 |
| gross_profit_factor | 1.1669 |
| gross_win_rate | 0.5402 |
| sharpe_ratio | -0.4254 |
| sortino_ratio | -0.1373 |
| max_drawdown | 0.2864 |
| cagr | -0.0674 |
| net_avg_win | 84.7523 |
| net_avg_loss | -106.5764 |
| avg_hold_time_bars | 26.8775 |
| exposure | 0.6084 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
