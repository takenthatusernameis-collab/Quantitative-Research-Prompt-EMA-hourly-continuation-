# EMA Hourly Continuation — AAVE/USDT P100_144

**Symbol:** AAVE/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 198 |
| net_profit_factor | 0.7943 |
| net_win_rate | 0.5152 |
| gross_profit_factor | 1.0606 |
| gross_win_rate | 0.5152 |
| sharpe_ratio | -1.0153 |
| sortino_ratio | -0.2057 |
| max_drawdown | 0.2491 |
| cagr | -0.0904 |
| net_avg_win | 80.1683 |
| net_avg_loss | -107.2351 |
| avg_hold_time_bars | 7.0808 |
| exposure | 0.0637 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
