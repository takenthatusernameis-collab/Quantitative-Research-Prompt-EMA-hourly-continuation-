# EMA Hourly Continuation — BTC/USDT P55_89

**Symbol:** BTC/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 679 |
| net_profit_factor | 0.2929 |
| net_win_rate | 0.3903 |
| gross_profit_factor | 1.0304 |
| gross_win_rate | 0.4786 |
| sharpe_ratio | -9.5291 |
| sortino_ratio | -3.3972 |
| max_drawdown | 0.9943 |
| cagr | -0.8361 |
| net_avg_win | 15.5402 |
| net_avg_loss | -33.9632 |
| avg_hold_time_bars | 4.2710 |
| exposure | 0.1160 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
