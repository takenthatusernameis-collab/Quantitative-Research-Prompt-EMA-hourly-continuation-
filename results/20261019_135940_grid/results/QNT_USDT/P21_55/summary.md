# EMA Hourly Continuation — QNT/USDT P21_55

**Symbol:** QNT/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1087 |
| net_profit_factor | 0.4001 |
| net_win_rate | 0.4489 |
| gross_profit_factor | 0.8232 |
| gross_win_rate | 0.4664 |
| sharpe_ratio | -8.4759 |
| sortino_ratio | -3.9364 |
| max_drawdown | 0.9927 |
| cagr | -0.8589 |
| net_avg_win | 13.5679 |
| net_avg_loss | -27.6260 |
| avg_hold_time_bars | 4.2935 |
| exposure | 0.2121 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
