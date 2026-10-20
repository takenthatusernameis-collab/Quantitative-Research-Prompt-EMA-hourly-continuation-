# EMA Hourly Continuation — DIA/USDT P12_89

**Symbol:** DIA/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 738 |
| net_profit_factor | 0.5903 |
| net_win_rate | 0.4621 |
| gross_profit_factor | 0.8816 |
| gross_win_rate | 0.4702 |
| sharpe_ratio | -4.5463 |
| sortino_ratio | -1.7229 |
| max_drawdown | 0.8840 |
| cagr | -0.5657 |
| net_avg_win | 37.0983 |
| net_avg_loss | -53.9813 |
| avg_hold_time_bars | 15.3022 |
| exposure | 0.5110 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
