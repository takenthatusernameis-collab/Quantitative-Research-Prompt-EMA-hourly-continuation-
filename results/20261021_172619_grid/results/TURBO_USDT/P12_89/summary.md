# EMA Hourly Continuation — TURBO/USDT P12_89

**Symbol:** TURBO/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 449 |
| net_profit_factor | 0.8268 |
| net_win_rate | 0.4944 |
| gross_profit_factor | 0.9844 |
| gross_win_rate | 0.4967 |
| sharpe_ratio | -1.4672 |
| sortino_ratio | -0.4865 |
| max_drawdown | 0.4421 |
| cagr | -0.2028 |
| net_avg_win | 81.1829 |
| net_avg_loss | -96.0282 |
| avg_hold_time_bars | 20.4209 |
| exposure | 0.5002 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
