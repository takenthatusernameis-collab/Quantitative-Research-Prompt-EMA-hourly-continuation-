# EMA Hourly Continuation — BOSON/USDT P50_89

**Symbol:** BOSON/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 683 |
| net_profit_factor | 0.5268 |
| net_win_rate | 0.4407 |
| gross_profit_factor | 0.8274 |
| gross_win_rate | 0.4524 |
| sharpe_ratio | -5.0765 |
| sortino_ratio | -1.8718 |
| max_drawdown | 0.8916 |
| cagr | -0.5864 |
| net_avg_win | 32.9597 |
| net_avg_loss | -49.2980 |
| avg_hold_time_bars | 5.2782 |
| exposure | 0.1639 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
