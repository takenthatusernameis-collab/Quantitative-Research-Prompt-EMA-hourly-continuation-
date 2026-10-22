# EMA Hourly Continuation — TAO/USDT P8_144

**Symbol:** TAO/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 549 |
| net_profit_factor | 0.7171 |
| net_win_rate | 0.4809 |
| gross_profit_factor | 0.9654 |
| gross_win_rate | 0.4827 |
| sharpe_ratio | -2.8940 |
| sortino_ratio | -0.9538 |
| max_drawdown | 0.7313 |
| cagr | -0.3678 |
| net_avg_win | 65.6668 |
| net_avg_loss | -84.8222 |
| avg_hold_time_bars | 28.4736 |
| exposure | 0.7105 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
