# EMA Hourly Continuation — GRT/USDT P89_144

**Symbol:** GRT/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 474 |
| net_profit_factor | 0.5100 |
| net_win_rate | 0.4641 |
| gross_profit_factor | 0.9650 |
| gross_win_rate | 0.4831 |
| sharpe_ratio | -4.7587 |
| sortino_ratio | -1.4689 |
| max_drawdown | 0.8423 |
| cagr | -0.5088 |
| net_avg_win | 39.4321 |
| net_avg_loss | -66.9718 |
| avg_hold_time_bars | 4.9304 |
| exposure | 0.1058 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
