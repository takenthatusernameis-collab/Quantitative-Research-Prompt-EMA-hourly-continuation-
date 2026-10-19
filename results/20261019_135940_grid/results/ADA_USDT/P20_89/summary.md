# EMA Hourly Continuation — ADA/USDT P20_89

**Symbol:** ADA/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 732 |
| net_profit_factor | 0.5393 |
| net_win_rate | 0.4713 |
| gross_profit_factor | 0.8989 |
| gross_win_rate | 0.4836 |
| sharpe_ratio | -4.7444 |
| sortino_ratio | -1.8096 |
| max_drawdown | 0.8923 |
| cagr | -0.5807 |
| net_avg_win | 30.1040 |
| net_avg_loss | -49.7629 |
| avg_hold_time_bars | 10.6817 |
| exposure | 0.3554 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
