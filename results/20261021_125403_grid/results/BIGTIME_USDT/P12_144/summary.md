# EMA Hourly Continuation — BIGTIME/USDT P12_144

**Symbol:** BIGTIME/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 365 |
| net_profit_factor | 0.9177 |
| net_win_rate | 0.5260 |
| gross_profit_factor | 1.1075 |
| gross_win_rate | 0.5260 |
| sharpe_ratio | -0.4822 |
| sortino_ratio | -0.1324 |
| max_drawdown | 0.2219 |
| cagr | -0.0631 |
| net_avg_win | 88.0643 |
| net_avg_loss | -106.5055 |
| avg_hold_time_bars | 41.5589 |
| exposure | 0.6864 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
