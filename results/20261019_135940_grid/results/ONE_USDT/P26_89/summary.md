# EMA Hourly Continuation — ONE/USDT P26_89

**Symbol:** ONE/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 688 |
| net_profit_factor | 0.6718 |
| net_win_rate | 0.4753 |
| gross_profit_factor | 0.9820 |
| gross_win_rate | 0.4826 |
| sharpe_ratio | -3.9574 |
| sortino_ratio | -1.4677 |
| max_drawdown | 0.8353 |
| cagr | -0.5018 |
| net_avg_win | 51.7132 |
| net_avg_loss | -69.7279 |
| avg_hold_time_bars | 11.3953 |
| exposure | 0.3564 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
