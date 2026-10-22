# EMA Hourly Continuation — OP/USDT P8_26

**Symbol:** OP/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1510 |
| net_profit_factor | 0.4266 |
| net_win_rate | 0.4609 |
| gross_profit_factor | 0.8928 |
| gross_win_rate | 0.4775 |
| sharpe_ratio | -8.7836 |
| sortino_ratio | -4.8187 |
| max_drawdown | 0.9975 |
| cagr | -0.9051 |
| net_avg_win | 10.6598 |
| net_avg_loss | -21.3664 |
| avg_hold_time_bars | 3.9781 |
| exposure | 0.2730 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
