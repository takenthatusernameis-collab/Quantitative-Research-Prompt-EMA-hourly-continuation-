# EMA Hourly Continuation — ZK/USDT P8_144

**Symbol:** ZK/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 439 |
| net_profit_factor | 0.8364 |
| net_win_rate | 0.4943 |
| gross_profit_factor | 0.9797 |
| gross_win_rate | 0.4966 |
| sharpe_ratio | -1.2313 |
| sortino_ratio | -0.3817 |
| max_drawdown | 0.3776 |
| cagr | -0.1633 |
| net_avg_win | 80.3959 |
| net_avg_loss | -93.9588 |
| avg_hold_time_bars | 32.7039 |
| exposure | 0.7000 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
