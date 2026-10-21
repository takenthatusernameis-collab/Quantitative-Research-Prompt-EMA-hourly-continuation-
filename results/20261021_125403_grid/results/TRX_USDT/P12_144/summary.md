# EMA Hourly Continuation — TRX/USDT P12_144

**Symbol:** TRX/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 399 |
| net_profit_factor | 0.6390 |
| net_win_rate | 0.5063 |
| gross_profit_factor | 1.0649 |
| gross_win_rate | 0.5188 |
| sharpe_ratio | -2.9314 |
| sortino_ratio | -0.8419 |
| max_drawdown | 0.6360 |
| cagr | -0.3202 |
| net_avg_win | 54.3922 |
| net_avg_loss | -87.2764 |
| avg_hold_time_bars | 32.8822 |
| exposure | 0.5964 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
