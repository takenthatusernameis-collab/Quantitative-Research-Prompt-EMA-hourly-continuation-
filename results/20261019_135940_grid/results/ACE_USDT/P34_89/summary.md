# EMA Hourly Continuation — ACE/USDT P34_89

**Symbol:** ACE/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 542 |
| net_profit_factor | 0.7616 |
| net_win_rate | 0.5203 |
| gross_profit_factor | 1.1561 |
| gross_win_rate | 0.5314 |
| sharpe_ratio | -2.0559 |
| sortino_ratio | -0.6826 |
| max_drawdown | 0.5839 |
| cagr | -0.2705 |
| net_avg_win | 62.1354 |
| net_avg_loss | -88.4943 |
| avg_hold_time_bars | 10.5517 |
| exposure | 0.2588 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
