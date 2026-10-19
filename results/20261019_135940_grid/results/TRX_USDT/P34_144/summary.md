# EMA Hourly Continuation — TRX/USDT P34_144

**Symbol:** TRX/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 484 |
| net_profit_factor | 0.3301 |
| net_win_rate | 0.3946 |
| gross_profit_factor | 0.9222 |
| gross_win_rate | 0.4773 |
| sharpe_ratio | -7.7317 |
| sortino_ratio | -2.4071 |
| max_drawdown | 0.9621 |
| cagr | -0.7262 |
| net_avg_win | 24.8049 |
| net_avg_loss | -48.9800 |
| avg_hold_time_bars | 15.0785 |
| exposure | 0.3317 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
