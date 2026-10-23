# EMA Hourly Continuation — NMR/USDT P20_100

**Symbol:** NMR/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 700 |
| net_profit_factor | 0.6782 |
| net_win_rate | 0.4857 |
| gross_profit_factor | 1.0065 |
| gross_win_rate | 0.4929 |
| sharpe_ratio | -3.9410 |
| sortino_ratio | -1.4611 |
| max_drawdown | 0.8388 |
| cagr | -0.5054 |
| net_avg_win | 51.4019 |
| net_avg_loss | -71.5826 |
| avg_hold_time_bars | 13.8943 |
| exposure | 0.4421 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
