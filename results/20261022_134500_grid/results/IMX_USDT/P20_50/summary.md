# EMA Hourly Continuation — IMX/USDT P20_50

**Symbol:** IMX/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 965 |
| net_profit_factor | 0.5256 |
| net_win_rate | 0.4715 |
| gross_profit_factor | 0.8935 |
| gross_win_rate | 0.4860 |
| sharpe_ratio | -5.8256 |
| sortino_ratio | -2.5258 |
| max_drawdown | 0.9580 |
| cagr | -0.7107 |
| net_avg_win | 23.2807 |
| net_avg_loss | -39.5195 |
| avg_hold_time_bars | 4.9430 |
| exposure | 0.2158 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
