# EMA Hourly Continuation — ID/USDT P12_144

**Symbol:** ID/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 450 |
| net_profit_factor | 0.7778 |
| net_win_rate | 0.5156 |
| gross_profit_factor | 1.0793 |
| gross_win_rate | 0.5222 |
| sharpe_ratio | -1.5534 |
| sortino_ratio | -0.4638 |
| max_drawdown | 0.4469 |
| cagr | -0.1994 |
| net_avg_win | 64.7954 |
| net_avg_loss | -88.6520 |
| avg_hold_time_bars | 33.6200 |
| exposure | 0.6847 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
