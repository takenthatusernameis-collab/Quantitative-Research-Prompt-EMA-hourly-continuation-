# EMA Hourly Continuation — XLM/USDT P20_89

**Symbol:** XLM/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 470 |
| net_profit_factor | 0.8187 |
| net_win_rate | 0.5298 |
| gross_profit_factor | 1.1155 |
| gross_win_rate | 0.5298 |
| sharpe_ratio | -1.2283 |
| sortino_ratio | -0.3843 |
| max_drawdown | 0.3997 |
| cagr | -0.1630 |
| net_avg_win | 65.3438 |
| net_avg_loss | -89.9252 |
| avg_hold_time_bars | 18.8745 |
| exposure | 0.4032 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
