# EMA Hourly Continuation — NUM/USDT P21_89

**Symbol:** NUM/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 705 |
| net_profit_factor | 0.5215 |
| net_win_rate | 0.3929 |
| gross_profit_factor | 0.7785 |
| gross_win_rate | 0.3957 |
| sharpe_ratio | -6.4725 |
| sortino_ratio | -2.4189 |
| max_drawdown | 0.9465 |
| cagr | -0.6843 |
| net_avg_win | 37.1688 |
| net_avg_loss | -46.1289 |
| avg_hold_time_bars | 11.7957 |
| exposure | 0.3780 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
