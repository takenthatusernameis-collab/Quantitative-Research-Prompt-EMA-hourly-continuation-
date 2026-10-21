# EMA Hourly Continuation — QNT/USDT P34_50

**Symbol:** QNT/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 235 |
| net_profit_factor | 0.6105 |
| net_win_rate | 0.4809 |
| gross_profit_factor | 0.9164 |
| gross_win_rate | 0.4809 |
| sharpe_ratio | -2.2972 |
| sortino_ratio | -0.5060 |
| max_drawdown | 0.4732 |
| cagr | -0.2059 |
| net_avg_win | 60.9696 |
| net_avg_loss | -92.4955 |
| avg_hold_time_bars | 5.4426 |
| exposure | 0.0581 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
