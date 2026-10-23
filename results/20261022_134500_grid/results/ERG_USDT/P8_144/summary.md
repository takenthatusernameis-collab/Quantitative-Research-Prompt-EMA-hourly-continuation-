# EMA Hourly Continuation — ERG/USDT P8_144

**Symbol:** ERG/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 666 |
| net_profit_factor | 0.4795 |
| net_win_rate | 0.4249 |
| gross_profit_factor | 0.7082 |
| gross_win_rate | 0.4309 |
| sharpe_ratio | -5.4853 |
| sortino_ratio | -1.9756 |
| max_drawdown | 0.9154 |
| cagr | -0.6199 |
| net_avg_win | 29.6820 |
| net_avg_loss | -45.7411 |
| avg_hold_time_bars | 22.1907 |
| exposure | 0.6718 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
