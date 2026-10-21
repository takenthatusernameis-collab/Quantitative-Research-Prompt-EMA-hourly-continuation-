# EMA Hourly Continuation — BSV/USDT P8_89

**Symbol:** BSV/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 593 |
| net_profit_factor | 0.6893 |
| net_win_rate | 0.4604 |
| gross_profit_factor | 0.8816 |
| gross_win_rate | 0.4604 |
| sharpe_ratio | -3.1430 |
| sortino_ratio | -1.0871 |
| max_drawdown | 0.7351 |
| cagr | -0.3934 |
| net_avg_win | 58.1016 |
| net_avg_loss | -71.9122 |
| avg_hold_time_bars | 21.6745 |
| exposure | 0.5842 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
