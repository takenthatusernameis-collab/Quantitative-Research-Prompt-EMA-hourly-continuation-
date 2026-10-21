# EMA Hourly Continuation — GRAM/USDT P21_144

**Symbol:** GRAM/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 382 |
| net_profit_factor | 0.6739 |
| net_win_rate | 0.4738 |
| gross_profit_factor | 0.8853 |
| gross_win_rate | 0.4738 |
| sharpe_ratio | -2.3220 |
| sortino_ratio | -0.6461 |
| max_drawdown | 0.5540 |
| cagr | -0.2567 |
| net_avg_win | 59.9555 |
| net_avg_loss | -80.1212 |
| avg_hold_time_bars | 26.9686 |
| exposure | 0.4683 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
