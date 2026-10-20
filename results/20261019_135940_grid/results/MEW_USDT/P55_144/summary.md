# EMA Hourly Continuation — MEW/USDT P55_144

**Symbol:** MEW/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 484 |
| net_profit_factor | 0.6019 |
| net_win_rate | 0.4525 |
| gross_profit_factor | 0.8203 |
| gross_win_rate | 0.4566 |
| sharpe_ratio | -3.5669 |
| sortino_ratio | -1.1083 |
| max_drawdown | 0.7410 |
| cagr | -0.4069 |
| net_avg_win | 50.4437 |
| net_avg_loss | -69.2596 |
| avg_hold_time_bars | 11.8326 |
| exposure | 0.2603 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
