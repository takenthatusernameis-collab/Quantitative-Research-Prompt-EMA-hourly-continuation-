# EMA Hourly Continuation — ACE/USDT P26_144

**Symbol:** ACE/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 412 |
| net_profit_factor | 0.6512 |
| net_win_rate | 0.4709 |
| gross_profit_factor | 0.9196 |
| gross_win_rate | 0.4806 |
| sharpe_ratio | -2.6804 |
| sortino_ratio | -0.7626 |
| max_drawdown | 0.6079 |
| cagr | -0.3052 |
| net_avg_win | 57.8270 |
| net_avg_loss | -79.0278 |
| avg_hold_time_bars | 26.5631 |
| exposure | 0.4952 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
