# EMA Hourly Continuation — BSV/USDT P21_144

**Symbol:** BSV/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 425 |
| net_profit_factor | 0.6287 |
| net_win_rate | 0.4353 |
| gross_profit_factor | 0.7940 |
| gross_win_rate | 0.4353 |
| sharpe_ratio | -3.2320 |
| sortino_ratio | -0.9419 |
| max_drawdown | 0.6645 |
| cagr | -0.3519 |
| net_avg_win | 60.7411 |
| net_avg_loss | -74.4683 |
| avg_hold_time_bars | 26.9624 |
| exposure | 0.5209 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
