# EMA Hourly Continuation — PYTH/USDT P12_89

**Symbol:** PYTH/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 752 |
| net_profit_factor | 0.5959 |
| net_win_rate | 0.4588 |
| gross_profit_factor | 0.8689 |
| gross_win_rate | 0.4628 |
| sharpe_ratio | -4.6494 |
| sortino_ratio | -1.7852 |
| max_drawdown | 0.8955 |
| cagr | -0.5789 |
| net_avg_win | 37.8665 |
| net_avg_loss | -53.8691 |
| avg_hold_time_bars | 15.0957 |
| exposure | 0.5160 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
