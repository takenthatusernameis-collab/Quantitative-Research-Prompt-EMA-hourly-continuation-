# EMA Hourly Continuation — XLM/USDT P100_144

**Symbol:** XLM/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 189 |
| net_profit_factor | 0.6001 |
| net_win_rate | 0.4815 |
| gross_profit_factor | 0.9169 |
| gross_win_rate | 0.4815 |
| sharpe_ratio | -2.0897 |
| sortino_ratio | -0.4130 |
| max_drawdown | 0.3829 |
| cagr | -0.1720 |
| net_avg_win | 62.2628 |
| net_avg_loss | -96.3378 |
| avg_hold_time_bars | 7.4233 |
| exposure | 0.0638 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
