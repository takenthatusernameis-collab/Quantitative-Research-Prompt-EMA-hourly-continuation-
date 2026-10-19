# EMA Hourly Continuation — DASH/USDT P21_144

**Symbol:** DASH/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 514 |
| net_profit_factor | 0.5491 |
| net_win_rate | 0.4630 |
| gross_profit_factor | 0.9160 |
| gross_win_rate | 0.4825 |
| sharpe_ratio | -3.7930 |
| sortino_ratio | -1.2152 |
| max_drawdown | 0.7756 |
| cagr | -0.4363 |
| net_avg_win | 39.0354 |
| net_avg_loss | -61.3037 |
| avg_hold_time_bars | 22.7821 |
| exposure | 0.5323 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
