# EMA Hourly Continuation — STX/USDT P34_89

**Symbol:** STX/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 437 |
| net_profit_factor | 0.7321 |
| net_win_rate | 0.4920 |
| gross_profit_factor | 0.9461 |
| gross_win_rate | 0.4920 |
| sharpe_ratio | -1.9024 |
| sortino_ratio | -0.5677 |
| max_drawdown | 0.4885 |
| cagr | -0.2291 |
| net_avg_win | 61.1702 |
| net_avg_loss | -80.9190 |
| avg_hold_time_bars | 10.5881 |
| exposure | 0.2094 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
