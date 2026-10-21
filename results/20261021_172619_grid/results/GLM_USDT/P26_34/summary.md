# EMA Hourly Continuation — GLM/USDT P26_34

**Symbol:** GLM/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 344 |
| net_profit_factor | 0.5546 |
| net_win_rate | 0.4680 |
| gross_profit_factor | 0.9351 |
| gross_win_rate | 0.4680 |
| sharpe_ratio | -3.8173 |
| sortino_ratio | -1.0185 |
| max_drawdown | 0.7154 |
| cagr | -0.3769 |
| net_avg_win | 53.7732 |
| net_avg_loss | -85.2981 |
| avg_hold_time_bars | 4.9041 |
| exposure | 0.0767 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
