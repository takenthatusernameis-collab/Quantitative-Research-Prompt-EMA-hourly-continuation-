# EMA Hourly Continuation — NOT/USDT P21_50

**Symbol:** NOT/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1039 |
| net_profit_factor | 0.5512 |
| net_win_rate | 0.4649 |
| gross_profit_factor | 0.8955 |
| gross_win_rate | 0.4735 |
| sharpe_ratio | -6.6716 |
| sortino_ratio | -3.0738 |
| max_drawdown | 0.9761 |
| cagr | -0.7777 |
| net_avg_win | 24.7710 |
| net_avg_loss | -39.0389 |
| avg_hold_time_bars | 3.9625 |
| exposure | 0.1934 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
