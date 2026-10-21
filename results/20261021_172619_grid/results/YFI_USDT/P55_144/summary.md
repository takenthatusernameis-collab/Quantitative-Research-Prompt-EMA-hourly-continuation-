# EMA Hourly Continuation — YFI/USDT P55_144

**Symbol:** YFI/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 420 |
| net_profit_factor | 0.6360 |
| net_win_rate | 0.4738 |
| gross_profit_factor | 0.9202 |
| gross_win_rate | 0.4738 |
| sharpe_ratio | -3.0236 |
| sortino_ratio | -0.8841 |
| max_drawdown | 0.6607 |
| cagr | -0.3332 |
| net_avg_win | 56.2225 |
| net_avg_loss | -79.5977 |
| avg_hold_time_bars | 14.1214 |
| exposure | 0.2684 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
