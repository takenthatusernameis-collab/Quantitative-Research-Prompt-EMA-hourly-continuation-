# EMA Hourly Continuation — ZRO/USDT P100_144

**Symbol:** ZRO/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 433 |
| net_profit_factor | 0.4353 |
| net_win_rate | 0.4319 |
| gross_profit_factor | 0.6998 |
| gross_win_rate | 0.4388 |
| sharpe_ratio | -4.8147 |
| sortino_ratio | -1.4709 |
| max_drawdown | 0.8110 |
| cagr | -0.5065 |
| net_avg_win | 33.2797 |
| net_avg_loss | -58.1186 |
| avg_hold_time_bars | 3.3995 |
| exposure | 0.0720 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
