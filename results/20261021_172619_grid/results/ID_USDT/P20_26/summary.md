# EMA Hourly Continuation — ID/USDT P20_26

**Symbol:** ID/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.6019 |
| net_win_rate | 0.4857 |
| gross_profit_factor | 0.9614 |
| gross_win_rate | 0.4857 |
| sharpe_ratio | -3.0391 |
| sortino_ratio | -0.8139 |
| max_drawdown | 0.6227 |
| cagr | -0.3127 |
| net_avg_win | 54.3955 |
| net_avg_loss | -85.3520 |
| avg_hold_time_bars | 4.4914 |
| exposure | 0.0711 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
