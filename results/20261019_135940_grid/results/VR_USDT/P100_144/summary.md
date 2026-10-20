# EMA Hourly Continuation — VR/USDT P100_144

**Symbol:** VR/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 615 |
| net_profit_factor | 0.3492 |
| net_win_rate | 0.2585 |
| gross_profit_factor | 0.6045 |
| gross_win_rate | 0.2683 |
| sharpe_ratio | -12.3020 |
| sortino_ratio | -4.4587 |
| max_drawdown | 0.9985 |
| cagr | -0.9236 |
| net_avg_win | 33.6996 |
| net_avg_loss | -33.6460 |
| avg_hold_time_bars | 4.0374 |
| exposure | 0.1129 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
