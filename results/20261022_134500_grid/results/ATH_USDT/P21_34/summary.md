# EMA Hourly Continuation — ATH/USDT P21_34

**Symbol:** ATH/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1044 |
| net_profit_factor | 0.4417 |
| net_win_rate | 0.4444 |
| gross_profit_factor | 0.8647 |
| gross_win_rate | 0.4646 |
| sharpe_ratio | -9.0046 |
| sortino_ratio | -4.2473 |
| max_drawdown | 0.9937 |
| cagr | -0.8820 |
| net_avg_win | 16.9382 |
| net_avg_loss | -30.6796 |
| avg_hold_time_bars | 2.3429 |
| exposure | 0.1186 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
