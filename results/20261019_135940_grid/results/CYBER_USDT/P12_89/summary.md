# EMA Hourly Continuation — CYBER/USDT P12_89

**Symbol:** CYBER/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 724 |
| net_profit_factor | 0.6684 |
| net_win_rate | 0.4848 |
| gross_profit_factor | 0.9795 |
| gross_win_rate | 0.4903 |
| sharpe_ratio | -3.6601 |
| sortino_ratio | -1.3823 |
| max_drawdown | 0.8156 |
| cagr | -0.4856 |
| net_avg_win | 46.6170 |
| net_avg_loss | -65.6284 |
| avg_hold_time_bars | 16.4820 |
| exposure | 0.5424 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
