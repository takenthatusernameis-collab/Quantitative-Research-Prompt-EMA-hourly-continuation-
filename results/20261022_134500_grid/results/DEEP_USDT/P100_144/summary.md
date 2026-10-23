# EMA Hourly Continuation — DEEP/USDT P100_144

**Symbol:** DEEP/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 346 |
| net_profit_factor | 0.5669 |
| net_win_rate | 0.4798 |
| gross_profit_factor | 0.9192 |
| gross_win_rate | 0.4884 |
| sharpe_ratio | -3.5584 |
| sortino_ratio | -1.0337 |
| max_drawdown | 0.6500 |
| cagr | -0.3980 |
| net_avg_win | 50.5164 |
| net_avg_loss | -82.1740 |
| avg_hold_time_bars | 4.4509 |
| exposure | 0.0872 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
