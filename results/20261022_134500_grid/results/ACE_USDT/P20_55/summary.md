# EMA Hourly Continuation — ACE/USDT P20_55

**Symbol:** ACE/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 765 |
| net_profit_factor | 0.5737 |
| net_win_rate | 0.4837 |
| gross_profit_factor | 0.9513 |
| gross_win_rate | 0.4928 |
| sharpe_ratio | -4.3964 |
| sortino_ratio | -1.7099 |
| max_drawdown | 0.8756 |
| cagr | -0.5574 |
| net_avg_win | 31.7209 |
| net_avg_loss | -51.7902 |
| avg_hold_time_bars | 7.4706 |
| exposure | 0.2586 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
