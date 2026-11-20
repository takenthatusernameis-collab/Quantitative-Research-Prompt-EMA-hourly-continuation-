# EMA Hourly Continuation — P2P/USDT P12_21

**Symbol:** P2P/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1394 |
| net_profit_factor | 0.2540 |
| net_win_rate | 0.2891 |
| gross_profit_factor | 0.5280 |
| gross_win_rate | 0.2941 |
| sharpe_ratio | -15.5451 |
| sortino_ratio | -8.2534 |
| max_drawdown | 1.0000 |
| cagr | -0.9853 |
| net_avg_win | 8.4476 |
| net_avg_loss | -13.5259 |
| avg_hold_time_bars | 3.0359 |
| exposure | 0.1924 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
