# EMA Hourly Continuation — XLM/USDT P12_89

**Symbol:** XLM/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 735 |
| net_profit_factor | 0.5250 |
| net_win_rate | 0.4966 |
| gross_profit_factor | 0.9709 |
| gross_win_rate | 0.5061 |
| sharpe_ratio | -4.3637 |
| sortino_ratio | -1.6511 |
| max_drawdown | 0.8785 |
| cagr | -0.5561 |
| net_avg_win | 26.3389 |
| net_avg_loss | -49.4946 |
| avg_hold_time_bars | 16.4748 |
| exposure | 0.5504 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
