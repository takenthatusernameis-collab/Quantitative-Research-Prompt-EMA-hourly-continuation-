# EMA Hourly Continuation — ENS/USDT P12_144

**Symbol:** ENS/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 340 |
| net_profit_factor | 0.8446 |
| net_win_rate | 0.5059 |
| gross_profit_factor | 1.0034 |
| gross_win_rate | 0.5059 |
| sharpe_ratio | -0.8460 |
| sortino_ratio | -0.2236 |
| max_drawdown | 0.3073 |
| cagr | -0.1000 |
| net_avg_win | 73.4151 |
| net_avg_loss | -88.9974 |
| avg_hold_time_bars | 46.4382 |
| exposure | 0.7177 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
