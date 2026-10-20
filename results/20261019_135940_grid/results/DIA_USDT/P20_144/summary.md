# EMA Hourly Continuation — DIA/USDT P20_144

**Symbol:** DIA/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 524 |
| net_profit_factor | 0.6711 |
| net_win_rate | 0.4866 |
| gross_profit_factor | 0.9747 |
| gross_win_rate | 0.4943 |
| sharpe_ratio | -2.7916 |
| sortino_ratio | -0.9028 |
| max_drawdown | 0.7087 |
| cagr | -0.3459 |
| net_avg_win | 52.6005 |
| net_avg_loss | -74.2990 |
| avg_hold_time_bars | 22.4809 |
| exposure | 0.5331 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
