# EMA Hourly Continuation — P2P/USDT P144_200

**Symbol:** P2P/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.4072 |
| net_win_rate | 0.3598 |
| gross_profit_factor | 0.5905 |
| gross_win_rate | 0.3598 |
| sharpe_ratio | -5.2444 |
| sortino_ratio | -1.3912 |
| max_drawdown | 0.8174 |
| cagr | -0.4863 |
| net_avg_win | 43.9345 |
| net_avg_loss | -60.6325 |
| avg_hold_time_bars | 6.0538 |
| exposure | 0.0971 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
