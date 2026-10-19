# EMA Hourly Continuation — XMR/USDT P26_89

**Symbol:** XMR/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1061 |
| net_profit_factor | 0.3780 |
| net_win_rate | 0.4185 |
| gross_profit_factor | 0.7907 |
| gross_win_rate | 0.4307 |
| sharpe_ratio | -9.2820 |
| sortino_ratio | -4.2444 |
| max_drawdown | 0.9955 |
| cagr | -0.8821 |
| net_avg_win | 13.6258 |
| net_avg_loss | -25.9372 |
| avg_hold_time_bars | 5.7314 |
| exposure | 0.2764 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
