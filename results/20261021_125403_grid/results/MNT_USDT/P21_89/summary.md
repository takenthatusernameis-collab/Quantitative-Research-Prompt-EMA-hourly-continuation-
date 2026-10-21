# EMA Hourly Continuation — MNT/USDT P21_89

**Symbol:** MNT/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 461 |
| net_profit_factor | 0.7587 |
| net_win_rate | 0.5119 |
| gross_profit_factor | 1.0258 |
| gross_win_rate | 0.5119 |
| sharpe_ratio | -1.7036 |
| sortino_ratio | -0.5249 |
| max_drawdown | 0.4955 |
| cagr | -0.2150 |
| net_avg_win | 60.6971 |
| net_avg_loss | -83.9121 |
| avg_hold_time_bars | 17.9892 |
| exposure | 0.3770 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
