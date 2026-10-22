# EMA Hourly Continuation — ZEC/USDT P55_89

**Symbol:** ZEC/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 666 |
| net_profit_factor | 0.4522 |
| net_win_rate | 0.4429 |
| gross_profit_factor | 0.8814 |
| gross_win_rate | 0.4535 |
| sharpe_ratio | -5.9793 |
| sortino_ratio | -2.1845 |
| max_drawdown | 0.9317 |
| cagr | -0.6534 |
| net_avg_win | 26.0232 |
| net_avg_loss | -45.7628 |
| avg_hold_time_bars | 3.3724 |
| exposure | 0.1021 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
