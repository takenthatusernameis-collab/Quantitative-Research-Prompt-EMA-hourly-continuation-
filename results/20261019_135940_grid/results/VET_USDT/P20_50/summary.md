# EMA Hourly Continuation — VET/USDT P20_50

**Symbol:** VET/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1006 |
| net_profit_factor | 0.5103 |
| net_win_rate | 0.4682 |
| gross_profit_factor | 0.9669 |
| gross_win_rate | 0.4821 |
| sharpe_ratio | -7.4906 |
| sortino_ratio | -3.3328 |
| max_drawdown | 0.9856 |
| cagr | -0.8132 |
| net_avg_win | 21.8016 |
| net_avg_loss | -37.6086 |
| avg_hold_time_bars | 4.3340 |
| exposure | 0.1982 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
