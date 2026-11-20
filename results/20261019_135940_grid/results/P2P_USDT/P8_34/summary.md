# EMA Hourly Continuation — P2P/USDT P8_34

**Symbol:** P2P/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1286 |
| net_profit_factor | 0.3368 |
| net_win_rate | 0.3569 |
| gross_profit_factor | 0.5145 |
| gross_win_rate | 0.3577 |
| sharpe_ratio | -10.4164 |
| sortino_ratio | -5.2170 |
| max_drawdown | 0.9984 |
| cagr | -0.9231 |
| net_avg_win | 11.0466 |
| net_avg_loss | -18.2037 |
| avg_hold_time_bars | 6.3033 |
| exposure | 0.3685 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
